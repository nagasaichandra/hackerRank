// https://www.hackerrank.com/challenges/mini-max-sum/problem
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func sum(arr []int64) int64 {
	sum := int64(0)
	for _, x := range arr {
		sum = sum + x
	}
	return sum
}

// Complete the miniMaxSum function below.
func miniMaxSum(nums []int64) {
	min := nums[1] + nums[2] + nums[3] + nums[4]
	max := min

	for i := 1; i < 5; i++ {
		sum := int64(0)
		for ii := 0; ii < 5; ii++ {
			if ii == i {
				continue
			}
			sum += nums[ii]
		}

		if sum < min {
			min = sum
		}

		if sum > max {
			max = sum
		}
	}

	fmt.Printf("%d %d", min, max)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	arrTemp := strings.Split(readLine(reader), " ")

	var arr []int64

	for i := 0; i < 5; i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int64(arrItemTemp)
		arr = append(arr, arrItem)
	}

	miniMaxSum(arr)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
