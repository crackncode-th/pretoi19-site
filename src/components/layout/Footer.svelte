<script lang="ts">
	import Facebook from "$components/icons/Facebook.svelte";
	import Instagram from "$components/icons/Instagram.svelte";
	import GitHub from "$components/icons/GitHub.svelte";
	import ext from "$lib/ext";
</script>

<footer class="mx-auto my-5 flex w-2/3 flex-col items-center justify-center">
	<hr class="mb-5 w-full" />
	<p>Crack 'n' Code Thailand</p>
	<p>"เดือนนี้คุณทำโจทย์ Crack 'n' Code แล้วหรือยัง"</p>
	<div class="icons flex flex-row justify-center gap-4">
		<a href="https://www.facebook.com/profile.php?id=100069611934421" {...ext}>
			<Facebook />
		</a>
		<a href="https://www.instagram.com/crackncodeth" {...ext}>
			<Instagram />
		</a>
		<a href="https://github.com/crackncode-th" {...ext}>
			<GitHub />
		</a>
	</div>
</footer>
