package help

import "strconv"

func IsNumeric(s string) bool {

	_, err := strconv.Atoi(s)
	return err == nil
}

func IsBoolean(s string) bool {

	_, err := strconv.ParseBool(s)
	return err == nil
}
