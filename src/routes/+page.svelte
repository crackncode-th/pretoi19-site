<script lang="ts">
	// import CncLogo from "$components/animated/CncLogo.svelte";
	import CncText from "$components/animated/CncText.svelte";
	import FloatIn from "$components/animated/FloatIn.svelte";
	import RedButton from "$components/elements/RedButton.svelte";
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
		<h2>
			Lorem ipsum, dolor sit amet consectetur adipisicing elit. Facere quidem placeat explicabo
			aperiam sunt nihil modi dolorem dolor? Ab animi at dolores odio quae repudiandae soluta
			consectetur modi officia iusto!
		</h2>
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
