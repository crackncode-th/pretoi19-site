<script lang="ts">
	import "$/app.scss";

	import NavBar from "$components/layout/NavBar.svelte";
	import Footer from "$components/layout/Footer.svelte";
</script>

<div class="relative overflow-x-hidden">
	<NavBar />
	<main class="min-h-[calc(100vh-18rem)] p-4 lg:min-h-[calc(100vh-16.5rem)]">
		<slot />
	</main>
	<Footer />
</div>
