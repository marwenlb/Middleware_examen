package users

import (
	"encoding/json"
	"net/http"
	"github.com/gofrs/uuid"
	"github.com/sirupsen/logrus"
	"middleware/example/internal/models"
	"middleware/example/internal/services/users"
)
type RequestBody struct {
	Username   string `json:"username"`
	Email      string `json:"email"`
	Premium    bool   `json:"premium"`
	Birthdate  string `json:"birthdate"`
	Country    string `json:"country"`
	// Add other necessary fields
}
// CreateUser creates a new user.
// Assumes that the User model structure is defined.
// @Tags         users
// @Summary      Create a new user.
// @Description  Creates a new user with provided details.
// @Accept       json
// @Produce      json
// @Param        requestBody   body     RequestBody   true  "User details"
// @Success      201           {object}       models.User
// @Failure      400           "Bad Request"
// @Failure      500           "Internal Server Error"
// @Router       /users [post]
func CreateUser(w http.ResponseWriter, r *http.Request) {

	type RequestBody struct {
		Username   string `json:"username"`
		Password string 	`json:"password"`
		Name     string 	`json:"name"`
		Email      string `json:"email"`
		Premium    bool   `json:"premium"`
		Birthdate  string `json:"birthdate"`
		Country    string `json:"country"`
	}

	var requestBody RequestBody
	err := json.NewDecoder(r.Body).Decode(&requestBody)
	if err != nil {
		logrus.Errorf("error decoding request body: %s", err.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	// Generate UUID for the user
	uuidCreated, err := uuid.NewV4()
	if err != nil {
		logrus.Errorf("error generating UUID: %s", err.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	// Create the user
	newUser := models.User{
		Id:        &uuidCreated,
		Username:  requestBody.Username,
		Password:  requestBody.Password,
		Name:  	   requestBody.Name,
		Email:     requestBody.Email,
		Premium:   requestBody.Premium,
		Birthdate: requestBody.Birthdate,
		Country:   requestBody.Country,
	}

	// Save the new user
	err = users.CreateUser(newUser)
	if err != nil {
		logrus.Errorf("error saving user: %s", err.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	responseBody, _ := json.Marshal(newUser)
	_, _ = w.Write(responseBody)
}
