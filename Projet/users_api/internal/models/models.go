package models

import (
	"github.com/gofrs/uuid"
)

type User struct {
	Id        *uuid.UUID `json:"id"`
	Username  string     `json:"username"`
	Password string 	`json:"password"`
	Name     string 	`json:"name"`
	Email     string     `json:"email"`
	Premium   bool       `json:"premium"`
	Birthdate string     `json:"birthdate"`
	Country   string     `json:"country"`
}