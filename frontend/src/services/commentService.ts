import { Comment } from "../types";
import axios from "axios";

const API_URL = "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
});

export const getComments = async () => {
  const response = await api.get("/comments/get");
  return response.data;
};

export const createComment = async (comment: Comment) => {
  const response = await api.post("/comments/create", comment);
  return response.data;
};

export const updateComment = async (comment: Comment) => {
  const response = await api.put(`/comments/update/${comment.id}`, comment);
  return response.data;
};

export const deleteComment = async (comment: Comment) => {
  const response = await api.delete(`/comments/delete/${comment.id}`);
  return response.data;
};
