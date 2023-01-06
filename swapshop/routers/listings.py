from fastapi import APIRouter, Depends, Response
from typing import Union,List, Optional
from queries.listings import Error, ListingIn, ListingOut, ListingQueries
router = APIRouter()

@router.get('/listings', response_model=Union[List[ListingOut], Error])
def get_listings(
    repo: ListingQueries = Depends(),
):
    return repo.get_listings()

@router.get('/listings/{listing_id}', response_model=Optional[ListingOut])
def get_one(
    listing_id: int,
    response: Response,
    repo: ListingQueries = Depends(),
) -> ListingOut:
    listing = repo.get_one(listing_id)
    if listing is None:
        response.status_code = 404
    return listing

@router.post('/listings', response_model=Union[ListingOut, Error])
def create_listing(listing: ListingIn, response:Response, repo: ListingQueries = Depends()):
    # if response.ok:
    response.status_code = 200
    return repo.create(listing)
    # else:
    #     response.status_code = 400
    #     return {"message": "Failed to create"}

@router.put('/listings/{listing_id}', response_model=Union[ListingOut, Error])
def update_listing(listing_id:int, listing:ListingIn, repo:ListingQueries=Depends(),) -> Union[Error, ListingQueries]:
    return repo.update(listing_id, listing)

@router.delete('/listings/{listing_id}', response_model=bool)
def delete_listing(listing_id: int, repo: ListingQueries = Depends(),) -> bool:
    return repo.delete(listing_id)