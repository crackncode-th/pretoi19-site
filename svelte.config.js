// @ts-check

import adapter from "@sveltejs/adapter-auto";
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
			$styles: path.resolve("src/styles")
		}
	}
};

export default config;
