import React, { useState } from "react";
import { deleteComment, updateComment } from "../services/commentService";

// comment is the parent/current comment that we are working with
// children is all the children comments in the form of Comment[]
const CommentBox = ({ comment, comments, setComments }) => {
  const [collapseChildren, setCollapseChildren] = useState(false);
  return (
    <div className="threadedComment" key={comment.id}>
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
              window.confirm("Are you sure you want to delete this comment?")
            ) {
              deleteComment(comment)
                .then(() => {
                  setComments(comments.filter((c) => c.id !== comment.id));
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
      {comment.children.length > 0 && (
        <div
          className="collapseButton"
          onClick={() =>
            setCollapseChildren((collapseChildren) => !collapseChildren)
          }
        >
          Collapse
        </div>
      )}
      {!collapseChildren && (
        <div>
          {comment.children.map((child) => (
            <div>
              <CommentBox
                comment={child}
                comments={comments}
                setComments={setComments}
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default CommentBox;
