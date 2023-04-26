<script lang="ts">
	import RedButton from "$components/elements/RedButton.svelte";
	import SponsorCard from "$components/elements/SponsorCard.svelte";
	import ext from "$lib/ext";

	import _sponsors from "$data/sponsors.json";

	import PrizeList from "$components/PrizeList.svelte";
	import CountDown from "$components/CountDown.svelte";

	import { serializeJsonLd, websiteSchema } from "$utils/json-ld";
</script>

<svelte:head>
	{@html serializeJsonLd(websiteSchema)}
</svelte:head>

<main class="page">
	<section>
		<h1 class="page-title mt-6">Crack 'n' Code x CodeBlitz</h1>
		<h1 class="page-title mt-2">Pre TOI19</h1>
	</section>

	<section>
		<div class="my-3 flex justify-center">
			<div class="h-2 w-11 bg-red-600" />
		</div>
	</section>

	<section>
		<h2>TOI ใกล้เข้ามาแล้ว อยากจะทดสอบฝีมือตัวเองใช่มั้ย คุณคิดว่าคุณพร้อมแค่ไหนกัน</h2>
	</section>

	<section>
		<h3 class="topic my-3">การแข่งขัน Pre-TOI19</h3>
		<h2>
			จะจัดขึ้นในวันที่ 13-14 พฤษภาคม 2566 ผ่านระบบ
			<span class="blue-link"><a href="https://cms-dev.github.io/" {...ext}>CMS</a></span>
		</h2>
		<h2>
			ซึ่งเป็นระบบเดียวกับที่ใช้ในการแข่งขันโอลิมปิกระดับชาติครั้งที่ 19 (TOI19) ที่จะมาถึงนี้
		</h2>
	</section>

	<section>
		<h3 class="topic mb-3 mt-5">เหลือเวลาสมัครอีก</h3>
		<CountDown />
	</section>

	<section>
		<div class="mb-6 mt-5 flex flex-col justify-center gap-5 sm:flex-row">
			<RedButton href="https://forms.gle/QtSv4pD7e92WEhVCA">Register</RedButton>
		</div>
	</section>

	<section>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic mt-5">รางวัล</h3>
		<PrizeList />
	</section>

	<section>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic mt-5">Powered by</h3>
		<div>
			<a href="https://web.facebook.com/xcodeblitz" {...ext}>
				<img src="/codeblitz.png" alt="CodeBlitz" class="mx-auto w-1/5" />
				<p class="text-center text-2xl">CodeBlitz</p>
			</a>
		</div>
	</section>

	<section>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic mt-5">Sponsors</h3>
		<div class="grid grid-cols-1 pt-4 sm:grid-cols-2 md:grid-cols-3">
			{#each _sponsors as sponsor}
				<div class="flex flex-col items-center justify-center gap-2 py-4 md:py-6">
					<SponsorCard href={sponsor.link}>
						{sponsor.name}
						<br />
						{sponsor.link}
					</SponsorCard>
				</div>
			{/each}
		</div>
	</section>
</main>

<style lang="postcss">
	h2 {
		@apply text-2xl;
	}
	.topic {
		@apply text-3xl font-bold;
	}
</style>
