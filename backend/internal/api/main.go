package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("this piece of shit better be working")
	router := gin.Default()
	router.GET("/test", func(ctx *gin.Context) {
		ctx.JSON(200, gin.H{
			"message": "this is a test mf",
		})
	})

	router.Run() // listen and serve on 0.0.0.0:8080
}
