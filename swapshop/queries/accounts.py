from pydantic import BaseModel
from .listings import ListingQueries
import os
from psycopg_pool import ConnectionPool
from typing import List, Union


pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class Error(BaseModel):
    message: str

class DuplicateAccountError(ValueError):
    message: str


class AccountIn(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class AccountOut(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str


class AccountOutWithPassword(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    hashed_password: str


class AccountQueries:
    #Region properties
    DB_NAME = "swapshop"
    COLLECTION = "accounts"


    def create(self, account: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # run our SELECT statement
                result = db.execute(
                    """
                    INSERT INTO accounts (email, hashed_password, first_name, last_name)
                    VALUES(%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [account.email, hashed_password, account.first_name, account.last_name]
                )
                id=result.fetchone()[0]
                return AccountOutWithPassword(
                    id=id,
                    email=account.email,
                    hashed_password=hashed_password,
                    first_name=account.first_name,
                    last_name=account.last_name,
                )


    def get_accounts(self) -> list[AccountOut]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id
                        , email
                        , first_name
                        , last_name
                    FROM accounts
                    """
                )
                
                return [self.record_to_account_out(record)
                for record in db.fetchall()
                ]


    def get_one(self, email: str) -> AccountOutWithPassword:
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our SELECT statement
                result = db.execute(
                    """
                    SELECT id
                            , email
                            , hashed_password
                            , first_name
                            , last_name
                    FROM accounts
                    WHERE email = %s
                    """,
                    [email],
                )
                record = result.fetchone()
                print(record)
                if record is None:
                    return None
                return AccountOutWithPassword(
                    id=record[0],
                    email=record[1],
                    hashed_password=record[2],
                    first_name=record[3],
                    last_name=record[4],
                )

    def get_one_id(self, account_id: int) -> AccountOutWithPassword:
        print(account_id)
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our SELECT statement
                result = db.execute(
                    """
                    SELECT id
                            , email
                            , hashed_password
                            , first_name
                            , last_name
                    FROM accounts
                    WHERE id = %s
                    """,
                    [account_id],
                )
                record = result.fetchone()
                print(record)
                if record is None:
                    return None
                return AccountOutWithPassword(
                    id=record[0],
                    email=record[1],
                    hashed_password=record[2],
                    first_name=record[3],
                    last_name=record[4],
                )

    def delete(self, account_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s
                        """,
                        [account_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def record_to_account_out(self, record):
        return AccountOut(
            id=record[0],
            email=record[1],
            first_name=record[2],
            last_name=record[3]
        )