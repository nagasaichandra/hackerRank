package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

// https://www.hackerrank.com/challenges/3d-surface-area/problem
// Complete the surfaceArea function below.
func surfaceArea(A [][]int32, H int, W int) int32 {
	h := H
	w := W
	var table [][]float64
	for i := 0; i < h+2; i++ {
		t := []float64{}
		for j := 0; j < w+2; j++ {
			t = append(t, 0)
		}
		table = append(table, t)
	}
	// fmt.Println(table)
	for i := 1; i < h+1; i++ {
		for j := 1; j < w+1; j++ {
			table[i][j] = float64(A[i-1][j-1])
		}
	}

	var area float64 = 2 * float64(h) * float64(w)

	for i := 1; i < h+1; i++ {
		for j := 1; j < w+1; j++ {
			area += math.Max(0, table[i][j]-table[i][j-1])
			area += math.Max(0, table[i][j]-table[i-1][j])
			area += math.Max(0, table[i][j]-table[i][j+1])
			area += math.Max(0, table[i][j]-table[i+1][j])
		}
	}

	return int32(area)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	HW := strings.Split(readLine(reader), " ")

	HTemp, err := strconv.ParseInt(HW[0], 10, 64)
	checkError(err)
	H := int32(HTemp)

	WTemp, err := strconv.ParseInt(HW[1], 10, 64)
	checkError(err)
	W := int32(WTemp)

	var A [][]int32
	for i := 0; i < int(H); i++ {
		ARowTemp := strings.Split(readLine(reader), " ")

		var ARow []int32
		for _, ARowItem := range ARowTemp {
			AItemTemp, err := strconv.ParseInt(ARowItem, 10, 64)
			checkError(err)
			AItem := int32(AItemTemp)
			ARow = append(ARow, AItem)
		}

		if len(ARow) != int(int(W)) {
			panic("Bad input")
		}

		A = append(A, ARow)
	}

	result := surfaceArea(A, int(H), int(W))

	fmt.Fprintf(writer, "%d\n", result)

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
