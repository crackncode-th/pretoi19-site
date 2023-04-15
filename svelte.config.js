// @ts-check

import adapter from "@sveltejs/adapter-static";
import { vitePreprocess } from "@sveltejs/kit/vite";
import path from "node:path";

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter: adapter(),
		alias: {
			"$/app.scss": path.resolve("src/app.scss"),
			$components: path.resolve("src/components"),
			$lib: path.resolve("src/lib"),
			$styles: path.resolve("src/styles"),
			$data: path.resolve("src/data"),
			$utils: path.resolve("src/utils")
		}
	}
};

export default config;
