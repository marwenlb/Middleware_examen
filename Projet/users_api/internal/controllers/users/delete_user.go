package users

import (
	"github.com/gofrs/uuid"
	"github.com/sirupsen/logrus"
	"middleware/example/internal/models"
	"middleware/example/internal/repositories/users"
	"net/http"
)

// DeleteUser deletes a user by ID.
// Assumes that the User model structure is defined.
// @Tags         users
// @Summary      Delete a user by ID.
// @Description  Deletes a user by ID.
// @Param        userId       path      string  true  "User UUID formatted ID"
// @Success      204          "No Content"
// @Failure      400          "Invalid UUID format"
// @Failure      404          "User not found"
// @Failure      500          "Internal Server Error"
// @Router       /users/{userId} [delete]

func DeleteUser(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	userID, ok := ctx.Value("userId").(uuid.UUID)
	if !ok {
		logrus.Error("Invalid UUID format")
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	// Récupérer l'utilisateur par ID
	user, err := users.GetUserByID(userID)
	if err != nil {
		switch err.(type) {
		case *models.NotFoundError:
			w.WriteHeader(http.StatusNotFound)
		default:
			logrus.Errorf("Error retrieving user: %s", err.Error())
			w.WriteHeader(http.StatusNotFound)
		}
		return
	}

	// Vérifier si l'utilisateur existe avant de le supprimer
	if user == nil {
		w.WriteHeader(http.StatusNotFound)
		return
	}

	// Supprimer l'utilisateur
	err = users.DeleteUser(userID)
	if err != nil {
		switch err.(type) {
		case *models.NotFoundError:
			w.WriteHeader(http.StatusNotFound)
		default:
			logrus.Errorf("Error deleting user: %s", err.Error())
			w.WriteHeader(http.StatusInternalServerError)
		}
		return
	}

	w.WriteHeader(http.StatusNoContent)
}
