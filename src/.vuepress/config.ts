import { defineUserConfig } from "vuepress";
import theme from "./theme.js";


export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "厦门大学 Course 题库",
      description: "一个收集厦门大学course.xmu.edu.cn题库的网站",
    },
  },

  theme,

  plugins: [
    
  ],

  // Enable it with pwa
  // shouldPrefetch: false,
});
