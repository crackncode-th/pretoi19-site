<script lang="ts">
	import TimeCard from "$components/elements/TimeCard.svelte";

	let wanted_time = new Date("2023-05-10T23:59:59+07:00").getTime();
	let current_time = new Date().getTime();
	let time_diff = Math.max(0, wanted_time - current_time);
	let day_list = getDayList(time_diff);

	function getDayList(t: number) {
		let day = Math.floor(t / (1000 * 60 * 60 * 24));
		let hour = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minute = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
		let second = Math.floor((t % (1000 * 60)) / 1000);
		return [day, hour, minute, second];
	}
	function updateTime() {
		current_time = new Date().getTime();
		time_diff = Math.max(0, wanted_time - current_time);
		day_list = getDayList(time_diff);
	}
	setInterval(updateTime, 1000);
</script>

<div class="flex justify-center font-bold md:text-3xl lg:text-5xl">
	<div class="flex flex-row">
		<TimeCard>
			{Math.floor(day_list[0] / 10)}
		</TimeCard>
		<TimeCard>
			{day_list[0] % 10}
		</TimeCard>
		<div class="border-[#101010] bg-[#101010] p-3">:</div>
		<TimeCard>
			{Math.floor(day_list[1] / 10)}
		</TimeCard>
		<TimeCard>
			{day_list[1] % 10}
		</TimeCard>
		<div class="border-[#101010] bg-[#101010] p-3">:</div>
		<TimeCard>
			{Math.floor(day_list[2] / 10)}
		</TimeCard>
		<TimeCard>
			{day_list[2] % 10}
		</TimeCard>
		<div class="border-[#101010] bg-[#101010] p-3">:</div>
		<TimeCard>
			{Math.floor(day_list[3] / 10)}
		</TimeCard>
		<TimeCard>
			{day_list[3] % 10}
		</TimeCard>
	</div>
</div>
