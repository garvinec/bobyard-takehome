import { useEffect, useState } from "react";
import "./App.css";
import { getComments, createComment } from "./services/commentService";
import CommentBox from "./components/Comment";

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
              .then((newCommentList) => {
                setComments(newCommentList);
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
        {/* nested map function in this div -> in the nested function, filter comments where parent == comment.id -> create a div for each child comment */}
        {comments.map((comment) => (
          <div className="commentBox" key={comment.id}>
            <CommentBox
              comment={comment}
              comments={comments}
              setComments={setComments}
            />
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
