package mecsol_test

import (
	"Mechanics/mecsol"
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestGran(t *testing.T) {
	Curv := mecsol.NewGranCurve(0.5, 1, 9)
	require.NotEmpty(t, Curv)

	CU, stats := Curv.UniCoefficient()

	require.IsType(t, 1.0, CU)
	require.IsType(t, "string", stats)

	CC, desc := Curv.CurvCoefficient()

	require.IsType(t, 1.0, CC)
	require.IsType(t, "string", desc)

	fmt.Println(CU)
	fmt.Println(CC)
	fmt.Println(stats, desc)
}
