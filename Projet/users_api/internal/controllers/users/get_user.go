package users

import (
	"encoding/json"
	"github.com/gofrs/uuid"
	"github.com/sirupsen/logrus"
	"middleware/example/internal/models"
	"middleware/example/internal/repositories/users"
	"net/http"
)

// GetUser retrieves a user by ID.
// Assumes that the User model structure is defined.
// @Tags         users
// @Summary      Get a user by ID.
// @Description  Retrieve a user by ID.
// @Param        userId       path      string  true  "User UUID formatted ID"
// @Success      200          {object}  models.User
// @Failure      404          "User not found"
// @Failure      500          "Internal Server Error"
// @Router       /users/{userId} [get]s
func GetUser(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	userID, _ := ctx.Value("userId").(uuid.UUID)

	user, err := users.GetUserByID(userID)
	if err != nil {
		logrus.Errorf("error: %s", err.Error())
		customError, isCustom := err.(*models.CustomError)
		if isCustom {
			w.WriteHeader(customError.Code)
			body, _ := json.Marshal(customError)
			_, _ = w.Write(body)
		} else {
			w.WriteHeader(http.StatusInternalServerError)
		}
		return
	}

	w.WriteHeader(http.StatusOK)
	body, _ := json.Marshal(user)
	_, _ = w.Write(body)
	return
}
