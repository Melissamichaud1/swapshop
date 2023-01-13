BEN'S DAILY JOURNAL

Day 1 - January 4
    Today was all sorts of challenging, and we basically
    spent the entirety of group time troubleshooting Docker
    Windows issues. This was critical as 3/5 of our group is
    on PC's. Jake, Cody, and Melissa shared for most of the day.

Day 2 - January 5
    Similar to yesterday, we unfortunately had a lot of wasted
    calories on frustrating setup errors. However, by the end
    of the day we were finally making some headway, having a
    couple of routes to show for it. We comtinued programming as
    a full group of 5, with Alonso at the reigns for much of the
    day. He was a huge help with our forward progress, I was the
    coder for the rest of the day.

Day 3 - January 6
    Happy Friday! I hopped into screensharing and being the coder/typer
    with the rest of the group helping spot my typos and errors. We
    made really good progress on auth and Cody took over for the last
    hour or so of the day.

Day 4 - January 9
    After finishing the last routes in our backend and auth all together, it was time to fill out our kanban (Trello) board in Notion and divvy up responsibilities. We decided who would be responsible (main programmer) for each of 10 pages and who would be either pair or trio (we have 5 members) programming with them. We decided which pages would be more challenging forst, assigning them to a trio in lieu of a pair. Then, we discussed the dependency of the pages. Like tomorrow, we're starting with the API and filtering sdince every single page depends on those functionalities.

    This gives us an organized, concise plan of attack for the coming days that was well thought out based on difficulty and dependencies.

Day 5 - January 10
    Melissa crafted a "shared work" journal in this directory for us as we worked all together on the backend from Day 1 to Day 4. We would switch drivers, team code, and tap Riley and SEIRs for assistance when necessary. After building part of the Main Page, Nav, and API integration/filter function all together, we jumped into our pair and trio programming assignments. We built these initial front end/React pages together first as they were critical to the building of all other pages. No API integration means no products to show which means... blank webpages even if we did everything correctly.

    So that seemed like the natural place to start!

    This took a LOT longer than originally thought. We switched off drivers, and while we intended to finish all of the API and filtering functions together today, we didn't get that far. We got hung up especially on the API integration for product items and pictures. We'll keep plugging away.

Day 6 - January 11
    We all planned on splitting off individually to start on our assigned pages, but... that didn't happen. Authorization continues to be hard, Riley was right about it being far and away the most challenging aspect of this build. Alonso drove for putting the finishing touches on the auth backend, while I drove for 2-3 hours working on the auth frontend. We had snags with many errors from "unprocessable entity" and accidently passing user credentials as a string instead of a handleSubmit object (thus putting plain text user data in the URL, oops), to silly issues like trying to log in with a wrong password. Need to work on an error message for that to make it more clear in the future. Not just a console.log, but an actually on screen error.

    Jake drove while working on a couple of Windows quirks, and Melissa continued work on our SwapShop logo.

    With help from Riley, Cooper, and Sarah we finally got our login function working with users created in Swagger. SUCCESS! That felt really good.

    It was another day of really solid work as a team, and I continue to be grateful for the talent of our group and our group dynamics. Folks are smart, willing to put in the work, and are investted in our success. That makes this 4 week project WAY more enjoyable. Things are coming along nicely!

Day 7 - January 12
    Today started with revamping our kanban/Trello board to get all of the team on the same page with future building of, well, pages. THe last two days we continued with a lot more one driver, four pairs of eyes, work than we thought we would originally. The decision to drop the API (way too hard to use to populate user data), hiccups in the auth process, and higher complexity of pages like signup and product filtering.

    But it was good to keep working together!

    After our standup, we put the finishing touches on the frontend signup and decided to punt filtering/search for the weekend and Monday. It feels like we're still in a good spot in terms of finishing on time.

    Once we had lunch, we hopped in a SEIR room because the signup page frontend was continuing to vex us. After an hour we found the capitalization error and things worked well. Once we came back from the hour long Google info session we made great headway on the Create Listing page. This isn't yet totally done, but 95% of the way there.

    Tomorrow we'll really (finally, I've had many false assumptions of how quickly we'd get through the backend and auth) dive into individual work. Definitely looking forward to that.

Day 8 - January 13

    Afterwards, we split up into our respective groups. Based on our order of importance (which page needed to be developed when), my first page was being Alonso's second pair of eyes on the Men's Page, and being primary programmer on the user Sale History Page. These pages however are later in our development timeline and Alonso was tied up being second for other pages, so I spent time reviewing Project Beta's functional components, and Candace's Redux and React Hooks lectures to allow me to more efficiently implement them when the time comes. I also looked ahead towards Websockets.

    Today's review focus was helpful and really increased my understanding. It was also a nice change of pace after a couple days of pushing hard through backend group work.

    So far it feels like we've been making great progress and are on track to finish this project in time without too much work outside of class time.