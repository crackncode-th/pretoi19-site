<script lang="ts">
	import RedButton from "$components/elements/RedButton.svelte";
	import CncLogo from "$components/animated/CncLogo.svelte";
	import CncText from "$components/animated/CncText.svelte";
	import FloatIn from "$components/animated/FloatIn.svelte";
</script>

<main>
	<CncLogo />
	<CncText delay={0} color="#F13830">
		<h1>404</h1>
	</CncText>
	<FloatIn delay={200}>
		<p class="my-5 text-xl">Sorry, we couldn't find that page.</p>
		<RedButton href="/">Home</RedButton>
	</FloatIn>
</main>

<style lang="postcss">
	h1 {
		@apply text-6xl font-bold;
	}
</style>
