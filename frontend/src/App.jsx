import { useEffect, useState } from "react";
import "./App.css";
import {
  getComments,
  createComment,
  updateComment,
  deleteComment,
} from "./services/commentService";
function App() {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    getComments().then((data) => setComments(data));
  }, []);

  return (
    <>
      <div>
        <h1>Bobyard Comments</h1>
      </div>
      <div className="createCommentSection">
        <button
          onClick={() => {
            const text = prompt("Enter your comment:");
            if (!text) return;

            const newComment = {
              author: "Admin",
              text,
              likes: 0,
            };

            createComment(newComment)
              .then((createdComment) => {
                setComments([...comments, createdComment]);
              })
              .catch((error) =>
                console.error("Error creating comment:", error)
              );
          }}
        >
          Add New Comment
        </button>
      </div>
      <div>
        {comments.map((comment) => (
          <div className="commentBox" key={comment.id}>
            <div className="commentAuthor">{comment.author}</div>
            <div className="commentDate">{comment.date}</div>
            <div className="commentText">{comment.text}</div>
            <div className="commentLikes">Likes: {comment.likes}</div>
            <div className="commentActions">
              <button
                onClick={() => {
                  const updatedText = prompt("Edit comment:", comment.text);
                  if (updatedText && updatedText !== comment.text) {
                    const updatedComment = { ...comment, text: updatedText };
                    updateComment(updatedComment)
                      .then(() => {
                        setComments(
                          comments.map((c) =>
                            c.id === comment.id ? updatedComment : c
                          )
                        );
                      })
                      .catch((error) =>
                        console.error("Error updating comment:", error)
                      );
                  }
                }}
              >
                Edit
              </button>
              <button
                onClick={() => {
                  if (
                    window.confirm(
                      "Are you sure you want to delete this comment?"
                    )
                  ) {
                    deleteComment(comment)
                      .then(() => {
                        setComments(
                          comments.filter((c) => c.id !== comment.id)
                        );
                      })
                      .catch((error) =>
                        console.error("Error deleting comment:", error)
                      );
                  }
                }}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
