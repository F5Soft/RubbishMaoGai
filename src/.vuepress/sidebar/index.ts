import { sidebar } from "vuepress-theme-hope";

export const Sidebar = sidebar({
  "": [
    {
      icon: "home",
      text: "首页",
      link: "/",
    },
    {
      icon: "blog",
      text: "题库",
      link: "/banks/",
      prefix: "/banks/",
      collapsible: true,
      children: "structure",
    },
  ],
});
