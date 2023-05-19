<script lang="ts">
	import _users from "$data/data.json";

	import Chevron from "$icons/Chevron.svelte";

	let users = _users;
	let anon = false;

	function filterUser(users: any[] | undefined): any[] {
		let response = [];
		for (let i = 0; i < users.length; i++) {
			if (users[i].Anonymous == 0) {
				response.push(users[i]);
			}
		}
		return response;
	}

	let filteredUsers = filterUser(_users);
	users = filteredUsers;

	function updateData() {
		if (anon) {
			users = filteredUsers;
			anon = false;
		} else {
			users = _users;
			anon = true;
		}
	}

	const gold_medal = 5;
	const silver_medal = 15;
	const bronze_medal = 30;

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

	<p class="text-3xl text-green-500">ผลคะแนนอย่างเป็นทางการ</p>

	<div class="mt-3 flex w-full justify-center text-xl">
		<input
			class="checked:border-primary checked:bg-primary dark:checked:border-primary dark:checked:bg-primary ml-[1.5rem] mr-[6px] mt-[0.15rem] h-[1.125rem] w-[1.125rem] appearance-none rounded-[0.25rem] border-[0.125rem] border-solid border-neutral-300 outline-none before:pointer-events-none before:absolute before:h-[0.875rem] before:w-[0.875rem] before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] checked:before:opacity-[0.16] checked:after:absolute checked:after:-mt-px checked:after:ml-[0.25rem] checked:after:block checked:after:h-[0.8125rem] checked:after:w-[0.375rem] checked:after:rotate-45 checked:after:border-[0.125rem] checked:after:border-l-0 checked:after:border-t-0 checked:after:border-solid checked:after:border-white checked:after:bg-transparent checked:after:content-[''] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:transition-[border-color_0.2s] focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] focus:after:absolute focus:after:z-[1] focus:after:block focus:after:h-[0.875rem] focus:after:w-[0.875rem] focus:after:rounded-[0.125rem] focus:after:content-[''] checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:after:-mt-px checked:focus:after:ml-[0.25rem] checked:focus:after:h-[0.8125rem] checked:focus:after:w-[0.375rem] checked:focus:after:rotate-45 checked:focus:after:rounded-none checked:focus:after:border-[0.125rem] checked:focus:after:border-l-0 checked:focus:after:border-t-0 checked:focus:after:border-solid checked:focus:after:border-white checked:focus:after:bg-transparent dark:border-neutral-600 dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"
			type="checkbox"
			value=""
			id="checkboxChecked"
			on:change={updateData}
		/>
		<p>แสดงผู้เข้าแข่งขันแบบ Anonymous</p>
	</div>
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
								{:else if column == "Rank"}
									{#if user["Anonymous"]}
										<span class="text-red-500">*</span>
									{:else}
										{user[column]}
									{/if}
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
	<p class="text-xl text-red-500">* Anonymous</p>
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
