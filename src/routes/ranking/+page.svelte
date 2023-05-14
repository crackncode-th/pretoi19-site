<script lang="ts">
	import _users from "$data/data.json";

	import Chevron from "$icons/Chevron.svelte";

	let users = _users;
	const gold_medal = 7;
	const silver_medal = 21;
	const bronze_medal = 40;

	const columns = [
		"Rank",
		"Name",
		"wordbuilder",
		"busan",
		"mineral",
		"Day 1",
		"mangoes",
		"oranges",
		"tourist",
		"Day 2",
		"Total"
	];

	function getMedalColor(rank: number) {
		// from THACO
		if (rank <= gold_medal) {
			return "bg-yellow-300";
		} else if (rank <= silver_medal) {
			return "bg-gray-300";
		} else if (rank <= bronze_medal) {
			return "bg-orange-300";
		}
		return "bg-sky-200";
	}

	let current_key = "Global";
	let ascending = false;

	function cmp<T>(a: T, b: T, key: string, flipped: boolean, fallback = "") {
		if (a[key] < b[key]) {
			return flipped ? 1 : -1;
		} else if (a[key] > b[key]) {
			return flipped ? -1 : 1;
		}
		return fallback ? cmp(a, b, fallback, true) : 0;
	}

	function sortKey(key: string) {
		return () => {
			if (key == current_key) {
				ascending = !ascending;
			} else {
				current_key = key;
				ascending = false;
			}

			users = users.sort((a, b) => cmp(a, b, key, !ascending, "Global"));
		};
	}
</script>

<main class="mx-auto">
	<h1 class="page-title">Ranking</h1>
	<p class="my-3">มีผู้เข้าแข่งขันที่ส่งแล้วได้คะแนน 80 ท่าน</p>

	<p class="text-3xl text-green-500">ผลคะแนนอย่างเป็นทางการ</p>

	<div class="wrapper mx-auto my-8 w-full overflow-x-scroll 2xl:w-[1250px]">
		<table class="mx-auto">
			<thead>
				{#each columns as column}
					<th
						class:selected-col={current_key == column}
						on:click={column == "Rank" ? null : sortKey(column)}
						class="min-w-[100px]"
					>
						<div>
							{column}
							{#if column != "Rank"}
								<Chevron ascending={ascending && current_key == column} />
							{/if}
						</div>
					</th>
				{/each}
			</thead>
			<tbody class="text-black">
				{#each users as user}
					<tr class={getMedalColor(user.Rank)}>
						{#each columns as column}
							<td class:font-bold={column.startsWith("Day") || column == "Total"}>
								{#if column == "Name" && user.Name == ""}
									<span class="text-slate-600">&lt;Anonymous&gt;</span>
								{:else}
									{user[column]}
								{/if}
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</main>

<style lang="postcss">
	th,
	td {
		@apply border p-1 text-base lg:p-2 lg:text-lg;
	}

	th {
		@apply cursor-pointer select-none transition-all;
	}

	th > div {
		@apply flex flex-row items-center justify-center gap-1;
	}

	.selected-col {
		@apply bg-pink-300 text-black;
	}
</style>
