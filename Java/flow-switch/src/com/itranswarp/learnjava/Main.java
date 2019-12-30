package com.itranswarp.learnjava;

import java.util.Scanner;

/**
 * switch实现石头/剪子/布并判断胜负
 */
public class Main {

	public static void main(String[] args) {
		System.out.println("please choice:");
		System.out.println(" 1: Rock");
		System.out.println(" 2: Scissors");
		System.out.println(" 3: Paper");
		Scanner scanner = new Scanner(System.in);
		// 用户输入:
		int choice = 0;
		choice = scanner.nextInt();
		// 计算机随机数 1, 2, 3:
		int random = 1 + (int) Math.random() * 3;
		System.out.println(random);
		int result = 0;
		switch (choice) {
		case 1 :
			if(random==3) {
				result = -1;
			}else if(random == choice) {
				result = 0;
			}else {
				result = 1;
			}
			break;
		case 2:
			if(random==1) {
				result = -1;
			}else if(random == choice) {
				result = 0;
			}else {
				result = 1;
			}
			break;
		case 3:
			if(random==1) {
				result = -1;
			}else if(random == choice) {
				result = 0;
			}else {
				result = 1;
			}
			break;
		}
		System.out.println(result);
	}

}
