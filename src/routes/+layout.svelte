<script lang="ts">
	import "$/app.scss";

	import NavBar from "$components/layout/NavBar.svelte";
	import Footer from "$components/layout/Footer.svelte";
</script>

<svelte:head>
	<title>Crack 'n' Code x CodeBlitz Pre TOI19</title>
	<meta
		name="description"
		content="การแข่งขัน Pre TOI19 จัดโดย Crack 'n' Code และ CodeBlitz ในวันที่ 13-14 พฤษภาคม 2566 เวลา 19.00-22.00 น."
	/>
</svelte:head>

<div class="relative overflow-x-hidden">
	<NavBar />
	<main class="min-h-[calc(100vh-18rem)] p-4 lg:min-h-[calc(100vh-16.5rem)]">
		<slot />
	</main>
	<Footer />
</div>
