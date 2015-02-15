// I have an array stock_prices_yesterday where:

// The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
// The values are the price of Apple stock at that time, in dollars.
// For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

// Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday. For this problem, we won't allow "shorting"-you must buy before you sell.

// src: https://www.interviewcake.com/question/stock-price

import java.lang.Math;

public class problem01_stock_price {
	public static void main(String[] args) {
		System.out.println("Max profit: " + get_best_profit(get_stock_price()));
	}

	static int get_best_profit(int[] stock) {
		int min_price = stock[0];
		int max_profit = 0;
		int current_price;

		for(int i = 0; i < stock.length; i++) {
			current_price = stock[i];
			min_price = Math.min(current_price, min_price);
			max_profit = Math.max(current_price - min_price, max_profit);
		}
		return max_profit;
	}

	static int[] get_stock_price(){
		int[] stock = new int[9*60];
		for(int i = 0; i < 9 * 60; i++) {
			stock[i] = i;
		}
		return stock;
	}
}