import { hopeTheme } from "vuepress-theme-hope";
import { Navbar } from "./navbar/index.js";
import { Sidebar } from "./sidebar/index.js";

export default hopeTheme({
  hostname: "https://banks.sherkey.ml/",
  iconAssets: "iconfont",
  logo: "/logo.svg",
  repo: "F5Soft/RubbishMaoGai",
  docsDir: "/src",
  locales: {
    "/": {
      navbar: Navbar,
      sidebar: Sidebar,
      displayFooter: false,
      metaLocales: {
        editLink: "在Github上编辑此页面",
      },
    },
  },
  fullscreen: true,
  backToTop: true,

  // encrypt: {
  //   
  // },

  plugins: {
    activeHeaderLinks: false,
    comment: {
      provider: "Waline",
      serverURL: "https://waline.sherkey.ml/",
    },

    components: {
      components: [
        "FontIcon",
      ],
    },

    mdEnhance: {
      align: true,
      attrs: true,
      container: true,
      gfm: true,
      imgLazyload: true,
      include: true,
      // playground: {
      //   presets: ["ts", "vue"],
      // },
      // presentation: {
      //   plugins: ["highlight", "math", "search", "notes", "zoom"],
      // },
      // stylize: [
      //   {
      //     matcher: "Recommended",
      //     replacer: ({ tag }) => {
      //       if (tag === "em")
      //         return {
      //           tag: "Badge",
      //           attrs: { type: "tip" },
      //           content: "Recommended",
      //         };
      //     },
      //   },
      // ],
      sub: true,
      sup: true,
      tabs: true,
      tasklist: true,
      vPre: true,
      vuePlayground: true,
    },

    photoSwipe: {
      scrollToClose: false,
      delay: 1000,
    },

    // pwa: {
    //   favicon: "/favicon.ico",
    //   cacheHTML: true,
    //   cachePic: true,
    //   appendBase: true,
    //   apple: {
    //     icon: "/assets/icon/apple-icon-152.png",
    //     statusBarColor: "black",
    //   },
    //   msTile: {
    //     image: "/assets/icon/ms-icon-144.png",
    //     color: "#ffffff",
    //   },
    //   manifest: {
    //     icons: [
    //       {
    //         src: "/assets/icon/chrome-mask-512.png",
    //         sizes: "512x512",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-mask-192.png",
    //         sizes: "192x192",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-512.png",
    //         sizes: "512x512",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-192.png",
    //         sizes: "192x192",
    //         type: "image/png",
    //       },
    //     ],
    //     shortcuts: [
    //       {
    //         name: "Demo",
    //         short_name: "Demo",
    //         url: "/demo/",
    //         icons: [
    //           {
    //             src: "/assets/icon/guide-maskable.png",
    //             sizes: "192x192",
    //             purpose: "maskable",
    //             type: "image/png",
    //           },
    //         ],
    //       },
    //     ],
    //   },
    // },
  },
});
