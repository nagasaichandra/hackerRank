package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'getWays' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. LONG_INTEGER_ARRAY c
 */

func getWays(n int, c []int) int {
	// Write your code here
	// Create table of size len(c)+1 and n+1
	table := make([][]int, len(c)+1)
	for row := 0; row <= len(c); row++ {
		row_ := []int{}

		for col := 0; col <= n; col++ {
			row_ = append(row_, 0)
		}
		table[row] = row_
		table[row][0] = 1
	}

	for r := 1; r <= len(c); r++ {
		for co := 1; co <= n; co++ {
			top := table[r-1][co]
			if co-c[r-1] < 0 {
				table[r][co] = top + 0
			} else {
				table[r][co] = top + table[r][co-c[r-1]]

			}
		}
	}
	fmt.Println(table)

	return table[len(c)][n]
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int(nTemp)

	mTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	m := int(mTemp)

	cTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var c []int

	for i := 0; i < int(m); i++ {
		cItem, err := strconv.ParseInt(cTemp[i], 10, 64)
		checkError(err)
		c = append(c, int(cItem))
	}

	// Print the number of ways of making change for 'n' units using coins having the values given by 'c'

	ways := getWays(n, c)

	fmt.Fprintf(writer, "%d\n", ways)

	writer.Flush()
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
