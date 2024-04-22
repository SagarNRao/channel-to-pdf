// flags: 1 for text 0 for image
// if starting with text: add a text component and keep a flag=1 and if the next message is a text then let the flag stay 1 and append to the text component, then if the next component is an image then set flag=0 and add an image component (and append if more images follow).
// arrayuse is the main array component that you append all the messages to, and text.tsx and image.tsx will also be a component similar to arrayuse, so you can append individual text and image files.

import { useState } from "react";
import { Text } from "./text.jsx";
import {Image} from "./image.jsx"

let arr = [];
let index = 0;
export default function Arrayuse()
{
    const [val, setval] = useState(arr);

    const Addnewtext = () => {
        arr.push(<Text key={index} />);
        index++;
        setval([...arr]);
    }
    const Addnewimage = () => {
        arr.push(<Image key={index} />);
        index++;
        setval([...arr]);
    }    

    return (
        <div>
            <p>{val}</p>
        </div>
    )
}