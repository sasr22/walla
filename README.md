# news.walla.co.il crawler

This project is made to iterate over 4,000,000 possible articales IDs in the news.walla.co.il news site.

This program is simple, it runs all the way from 0 to 4 milion using 40 threads all doing 100,000 requests to speed up things.

In order to start just install the requirement.txt file for the dependencies and run the `main.py` file.

This program knows to start from where it stopped in order to not loose progress.