import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";

export async function GET(request){
    try {
        const url = new URL(request.url);
        const userId = url.searchParams.get('userId');
        const result = await prisma.SavedBouquet.findMany({
            where : {
                userId: userId
            },
        })
        console.log("hit!");
        const bouquetsList = result.map(bouquet => ({
            id: String(bouquet.id),
            bouquet: JSON.parse(bouquet.bouquet),
            userId: bouquet.userId,
            user: bouquet.user
        }));
        return NextResponse.json({ bouquets: bouquetsList }, { status: 200 });
    } catch (error){
        console.error("Error creating user:", error);
        return NextResponse.json({ status: "error", error: error.message }, { status: 500 });
    }
}