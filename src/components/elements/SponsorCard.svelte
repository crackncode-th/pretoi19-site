<script lang="ts">
	import Link from "$components/elements/Link.svelte";
	import styles from "$styles/styles.module.scss";

	export let href: string;
</script>

<Link {href}>
	<div class="bg-slate-800 py-3 text-white hover:bg-red-500 {styles.colorButton}">
		<slot />
	</div>
</Link>
