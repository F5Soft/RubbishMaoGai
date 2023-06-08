import { defineUserConfig } from "vuepress";
import theme from "./theme.js";


export default defineUserConfig({
  base: "/RubbishMaoGai/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "厦门大学 Course 题库",
      description: "一个收集厦门大学 course.xmu.edu.cn 题库的网站",
    },
  },

  theme,

  plugins: [],

  // Enable it with pwa
  // shouldPrefetch: false,
});
