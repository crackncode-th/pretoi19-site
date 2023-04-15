<script>
	import Card from "$components/elements/Card.svelte";
</script>

<div class="grid grid-cols-1 gap-3 pt-5">
	<div>
		<h2 class="top-prize">คะแนนรวมสูงสุด 16 อันดับแรก</h2>
		<Card>
			<div class="p-5">
				<div class="flex justify-center">
					<img src="/pretoi-shirt.png" class="" alt="first place prize" />
				</div>
				<p class="pt-2 text-2xl">เสื้อ Crack 'n' Code X CodeBlitz</p>
			</div>
		</Card>
	</div>
</div>

<style lang="postcss">
	h2 {
		@apply text-2xl;
	}
	.top-prize {
		@apply font-bold text-red-500;
	}
</style>
