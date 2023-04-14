<script lang="ts">
	import Facebook from "$components/icons/Facebook.svelte";
	import Instagram from "$components/icons/Instagram.svelte";
	import GitHub from "$components/icons/GitHub.svelte";
	import ext from "$lib/ext";
</script>

<footer class="mx-auto my-5 flex w-2/3 flex-col items-center justify-center">
	<hr class="mb-5 w-full" />
	<h3 class="text-lg font-bold">Crack 'n' Code Thailand</h3>
	<p>"เดือนนี้คุณทำโจทย์ Crack 'n' Code แล้วหรือยัง"</p>
	<div class="grid grid-cols-3 font-bold text-slate-400">
		<div>
			<a href="contact">
				<p class="">Contact Us</p>
			</a>
		</div>
		<div>
			<p class="">|</p>
		</div>
		<div>
			<a href="about">
				<p class="">About</p>
			</a>
		</div>
	</div>
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
