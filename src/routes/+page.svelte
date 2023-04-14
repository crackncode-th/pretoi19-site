<script lang="ts">
	import CncText from "$components/animated/CncText.svelte";
	import FloatIn from "$components/animated/FloatIn.svelte";
	import RedButton from "$components/elements/RedButton.svelte";
	import SponsorCard from "$components/elements/SponsorCard.svelte";
	import ext from "$lib/ext";

	import _sponsors from "$data/sponsors.json";

	import PrizeList from "$components/PrizeList.svelte";
	import CountDown from "$components/CountDown.svelte";
</script>

<svelte:head>
	<title>Crack 'n' Code x CodeBlitz Pre TOI19</title>
	<meta name="description" content="Crack 'n' Code is online programming contest organizer" />
</svelte:head>

<main class="page">
	<CncText delay={0} clsx="mb-10" color="#F13830">
		<h1 class="page-title mt-6">Crack 'n' Code x CodeBlitz</h1>
		<h1 class="page-title mt-2">Pre TOI19</h1>
	</CncText>

	<CncText delay={0} clsx="my-6" color="#101010">
		<div class="h-2 w-11 bg-red-600" />
	</CncText>

	<CncText delay={0} clsx="mb-5" color="#F13830">
		<h2>TOI ใกล้เข้ามาแล้ว อยากจะทดสอบฝีมือตัวเองใช่มั้ย คุณคิดว่าคุณพร้อมแค่ไหนกัน</h2>
	</CncText>

	<FloatIn delay={200}>
		<h3 class="topic my-3">การแข่งขัน Pre-TOI19</h3>
		<h2>
			จะจัดขึ้นในวันที่ 13-14 พฤษภาคม 2566 ผ่านระบบ
			<span class="blue-link"><a href="https://cms-dev.github.io/" {...ext}>CMS</a></span>
		</h2>
		<h2>
			ซึ่งเป็นระบบเดียวกับที่ใช้ในการแข่งขันโอลิมปิกระดับชาติครั้งที่ 19 (TOI19) ที่จะมาถึงนี้
		</h2>
	</FloatIn>

	<FloatIn delay={200}>
		<h3 class="topic mb-3 mt-5">เหลือเวลาสมัครอีก</h3>
		<CountDown />
	</FloatIn>

	<FloatIn delay={400}>
		<div class="mb-6 mt-5 flex flex-col justify-center gap-5 sm:flex-row">
			<RedButton href="/">Register</RedButton>
		</div>
	</FloatIn>

	<FloatIn delay={600}>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic mt-5">รางวัล</h3>
		<PrizeList />
	</FloatIn>

	<FloatIn delay={800}>
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
	</FloatIn>

	<FloatIn delay={800}>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic mt-5">Sponsors</h3>
		<div class="grid grid-cols-1 pt-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
			{#each _sponsors as sponsor}
				<div class="flex flex-col items-center justify-center py-4 md:py-6">
					<SponsorCard href={sponsor.link}>
						{sponsor.name}
						<br />
						{sponsor.link}
					</SponsorCard>
				</div>
			{/each}
		</div>
	</FloatIn>
</main>

<style lang="postcss">
	h2 {
		@apply text-2xl;
	}
	.topic {
		@apply text-3xl font-bold;
	}
</style>
