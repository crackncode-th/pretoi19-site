<script lang="ts">
	import "$/app.scss";

	import NavBar from "$components/layout/NavBar.svelte";
</script>

<NavBar />
<main class="min-h-[calc(100vh-18rem)] p-4">
	<slot />
</main>
<footer class="mx-auto my-5 flex w-2/3 flex-col items-center justify-center">
	<hr class="mb-5 w-full" />
	<p>Crack 'n' Code Thailand</p>
	<p>"เดือนนี้คุณทำโจทย์ Crack 'n' Code แล้วหรือยัง"</p>
</footer>
