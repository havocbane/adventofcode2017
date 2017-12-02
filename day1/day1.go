package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func inverseCaptcha(str string) int64 {
	var sum int64
	i, sum := 0, 0
	size := len(str)

	last, err := strconv.ParseInt(string(str[size-1]), 10, 64)
	check(err)

	for i < size-2 {
		cur, err := strconv.ParseInt(string(str[i]), 10, 64)
		check(err)

		if cur^last == 0 {
			sum += last
		}
		last = cur
		i++
	}
	return sum
}

func inverseCaptchaPart2(str string) int64 {
	var sum int64
	i, sum := 0, 0
	size := len(str)
	half := int(size / 2)

	for i < size {
		j := i + half
		if j >= size {
			j -= size
		}

		cur, err := strconv.ParseInt(string(str[i]), 10, 64)
		check(err)

		half, err := strconv.ParseInt(string(str[j]), 10, 64)
		check(err)

		if cur^half == 0 {
			sum += half
		}
		i++
	}
	return sum
}

/*
$ go run day1.go
Result: 1177, time: 93.075µs
Result Part 2: 1060, time: 152.004µs

$ python day1.py
<function inverse_captcha at 0x10ed8de18> result: 1177, time 0.0012671947479248047
<function inverse_captcha_halfway at 0x10efb7378> result: 1060, time 0.0013959407806396484

... HOLY GUACAMOLE!
*/
func main() {
	dat, err := ioutil.ReadFile("input.txt")
	check(err)
	str := string(dat)
	str = strings.TrimSpace(str)

	start := time.Now()
	result := inverseCaptcha(str)
	elapsed := time.Since(start)

	fmt.Printf("Result: %v, time: %s", result, elapsed)

	start = time.Now()
	result = inverseCaptchaPart2(str)
	elapsed = time.Since(start)

	fmt.Printf("\nResult Part 2: %v, time: %s", result, elapsed)
}
