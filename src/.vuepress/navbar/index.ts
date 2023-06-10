import { navbar } from "vuepress-theme-hope";

export const Navbar = navbar([
  { 
    text: "首页", 
    icon: "home", 
    link: "/" 
  },
  { 
    text: "题库", 
    icon: "blog", 
    link: "/banks/",
    prefix: "/banks/",
    children: [
      "mg", 
      "my",
      "sg",
    ], 
  },
]);
