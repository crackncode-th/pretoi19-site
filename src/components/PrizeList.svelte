<script>
	import Card from "$components/elements/Card.svelte";
</script>

<div class="grid grid-cols-1 gap-3 pt-5">
	<!--
	<div>
		<h2 class="top-prize">คะแนนรวมสูงสุดอันดับ 1</h2>
		<Card>
			<div class="p-5">
				<div class="flex justify-center">
					<img src="/crackncode.webp" class="w-1/2" alt="first place prize" />
				</div>
				<p class="pt-3 text-2xl">รางวัลอันดับที่ 1</p>
				<p class="pt-2 text-xl text-gray-400">Prize Detail</p>
			</div>
		</Card>
	</div>
	<div>
		<h2 class="top-prize">คะแนนรวมสูงสุดอันดับ 2</h2>
		<Card>
			<div class="p-5">
				<div class="flex justify-center">
					<img src="/crackncode.webp" class="w-1/2" alt="first place prize" />
				</div>
				<p class="pt-3 text-2xl">รางวัลอันดับที่ 2</p>
				<p class="pt-2 text-xl text-gray-400">Prize Detail</p>
			</div>
		</Card>
	</div>
	<div>
		<h2 class="top-prize">คะแนนรวมสูงสุดอันดับ 3</h2>
		<Card>
			<div class="p-5">
				<div class="flex justify-center">
					<img src="/crackncode.webp" class="w-1/2" alt="first place prize" />
				</div>
				<p class="pt-3 text-2xl">รางวัลอันดับที่ 3</p>
				<p class="pt-2 text-xl text-gray-400">Prize Detail</p>
			</div>
		</Card>
	</div>
  -->
	<div>
		<h2 class="top-prize">คะแนนรวมสูงสุด 16 อันดับแรก</h2>
		<Card>
			<div class="p-5">
				<div class="flex justify-center">
					<img src="/pretoi-shirt.png" class="" alt="first place prize" />
				</div>
				<p class="pt-3 text-2xl">รางวัลอันดับที่ 1-16</p>
				<p class="pt-2 text-xl text-gray-400">Prize Detail</p>
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
