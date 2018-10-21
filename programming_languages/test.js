var a = 0.0

for (i= 0; i < 1000; i++)
{
	a += 0.1
	console.log(a)
}

var b = 11111111111111111111111111.1
var c = 11111111111111111111111111.0
console.log("Потеря значимости: ", b - c)

var ar = [1, 2, 4]
console.log(ar[0])
