import type { Thing, WithContext, Event } from "schema-dts";

export type Schema = Thing | WithContext<Thing>;

export function serializeJsonLd(data: Schema): string {
	return `<script type="application/ld+json">${JSON.stringify(data, null, 2)}</script>`;
}

export const websiteSchema: WithContext<Event> = {
	"@context": "https://schema.org",
	"@type": "Event",
	name: "Crack 'n' Code x CodeBlitz Pre TOI19",
	startDate: "2023-05-14",
	location: {
		"@type": "Place",
		name: "ผ่านระบบ CMS"
	},
	image: "https://pretoi19.crackncode.org/cncxcodeblitz.png",
	description:
		"การแข่งขัน TOI19 ใกล้เข้ามาแล้ว อยากจะทดสอบฝีมือตัวเองใช่มั้ย คุณคิดว่าคุณพร้อมแค่ไหนกัน",
	url: "https://forms.gle/QtSv4pD7e92WEhVCA",
	performer: {
		"@type": "Person",
		name: "Crack n code x codeblitz"
	},
	offers: {
		"@type": "Offer",
		price: "รางวัล คะแนนรวมสูงสุด 16 อันดับแรก [first place prize] เสื้อ Crack 'n' Code X CodeBlitz"
	}
};
