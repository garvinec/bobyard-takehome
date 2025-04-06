export interface Comment {
  id: number;
  author: string;
  children: Comment[];
  text: string;
  date: string;
  likes: number;
}
