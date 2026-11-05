# Used Phones Data Analysis

For this assignment, I wanted to see what the data could tell me about used phone prices. I started by checking for missing values and duplicates. Then I looked at how long the devices had been used, how their prices were spread out, and which devices had unusually high or low prices. I also ran a regression to see how things like storage, battery, weight, and days used relate to the normalized used price.

## How to run it

1. Put `used_device_data.csv` from the assignment ZIP in the same folder as the notebook.
2. Install what you need with `python -m pip install jupyter pandas numpy matplotlib statsmodels`.
3. Open the notebook and change the line that loads the data to `pd.read_csv("used_device_data.csv")`.
4. Run the cells from top to bottom.

## Practice code

Run `python used_phones_practice.py used_device_data.csv` to compare prices by 5G label and see how the average price from a sample compares with the average for the full dataset. It also saves a histogram called `used_price_histogram.png`.

## Things to double-check

- Check how 5G is labeled in the CSV. The saved results suggest the current 5G code gives every row the same value, so the regression can't estimate a slope for it.
- Check the assignment prompt for Question 6. The notebook goes from Question 5 to Question 7.
- Before turning it in, save the notebook with the comments and outputs showing. Check whether the practice file can be submitted separately.
