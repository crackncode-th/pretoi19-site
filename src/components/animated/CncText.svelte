<script lang="ts">
	import { onMount } from "svelte";
	import { doubleSlide, doubleSlide_txt } from "$lib/transitions";
	export let clsx = "";
	export let delay: number;
	export let color: string;
	export let duration = 1500;
	let showElement = false;
	onMount(() => {
		showElement = true;
	});
</script>

{#if showElement}
	<div class="center-itself container items-center {clsx}">
		<div class="box" transition:doubleSlide|local={{ delay, duration, color }} />
		<p
			class="center-itself"
			transition:doubleSlide_txt|local={{
				delay,
				duration
			}}
		>
			<slot />
		</p>
	</div>
{/if}

<style lang="scss">
	.box {
		width: 100%;
		height: 100%;
		background-color: transparent;
		z-index: -1;
		position: fixed;
		left: 0%;
	}
	.container {
		width: fit-content;
		height: fit-content;
	}
	.center-itself {
		position: relative;
		transform: translateX(-50%);
		left: 50%;
	}
</style>
