import { SignIn } from "@clerk/nextjs";
import Image from "next/image";
import Navbar from "@/components/Navbar";

export default function SignInPage() {
  return (
    <main className="flex-col flex items-center w-full ">
      <Navbar />
      <div className="flex flex-col justify-center items-center mt-24 scale-125 ">
        <SignIn />
      </div>
    </main>
  );
}
