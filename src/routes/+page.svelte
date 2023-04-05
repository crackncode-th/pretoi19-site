<script lang="ts">
	// import CncLogo from "$components/animated/CncLogo.svelte";
	import CncText from "$components/animated/CncText.svelte";
	import FloatIn from "$components/animated/FloatIn.svelte";
	import RedButton from "$components/elements/RedButton.svelte";
	import SponsorCard from "$components/elements/SponsorCard.svelte";

	import _sponsors from "$data/sponsors.json";
</script>

<svelte:head>
	<title>Crack 'n' Code Thailand</title>
	<meta name="description" content="Crack 'n' Code is online programming contest organizer" />
</svelte:head>

<main class="page">
	<CncText delay={0} clsx="mb-10" color="#F13830">
		<h1 class="page-title mt-6">Crack 'n' Code Pre TOI19</h1>
	</CncText>

	<CncText delay={0} clsx="my-6" color="#101010">
		<div class="h-2 w-11 bg-red-600" />
	</CncText>

	<CncText delay={0} clsx="mb-5" color="#F13830">
		<h2>
			Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet dicta dolores quae laborum
			nemo cumque labore animi illum, laudantium, quam facere distinctio fugiat doloremque. Saepe,
			sed? Asperiores atque nesciunt animi?
		</h2>
	</CncText>

	<FloatIn delay={400}>
		<div class="mb-6 mt-11 flex flex-col justify-center gap-5 sm:flex-row">
			<RedButton href="/">Register</RedButton>
		</div>
	</FloatIn>

	<FloatIn delay={600}>
		<div class="mt-3 flex justify-center">
			<hr class="w-3/4" />
		</div>
		<h3 class="topic my-5">Sponsors</h3>
		<div class="grid grid-cols-1 pt-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
			{#each _sponsors as sponsor, key}
				<div class="flex flex-col items-center justify-center py-4 md:py-8">
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
