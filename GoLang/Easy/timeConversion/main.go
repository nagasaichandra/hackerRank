package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// https://www.hackerrank.com/challenges/time-conversion/problem
/*
 * Complete the timeConversion function below.
 */
func timeConversion(s string) string {
	/*
	 * Write your code here.
	 */
	if s[:2] == "12" && s[len(s)-2:] == "AM" {
		return "00" + s[2:len(s)-2]
	}
	if s[len(s)-2:] == "AM" || s[:2] == "12" {
		return s[:len(s)-2]
	}
	if s[len(s)-2:] == "PM" {
		i, _ := strconv.Atoi(s[:2])
		x := i + 12

		return string(strconv.Itoa(x) + s[2:len(s)-2])
	}
	return s

}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	outputFile, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer outputFile.Close()

	writer := bufio.NewWriterSize(outputFile, 1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Fprintf(writer, "%s\n", result)

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
