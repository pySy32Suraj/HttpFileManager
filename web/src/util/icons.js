// By type
import audio_icon from "../res/audio.png";
import compressed_icon from "../res/compressed.png";
import document_icon from "../res/document.png";
import image_icon from "../res/image.png";
import video_icon from "../res/video.png";

// By extensions

// * for documents
import document_icon_pdf from "../res/pdf.png";
import document_icon_ppt from "../res/ppt.png";
import document_icon_txt from "../res/txt.png";
import document_icon_xls from "../res/xls.png";
import document_icon_doc from "../res/doc.png";

// for Unknown file type
import file_unknown from "../res/unknown.png";

// Folder icons
import fill_folder_icon from "../res/fill-folder.png";
import empty_folder_icon from "../res/empty-folder.png";



const file_folder_icons = {
    audio: {
        formatName: "audio",
        exts: [".mp3"], 
        icons: {

            default: audio_icon,
        },

    },
    video: {
        formatName: "video",
        exts: [".mp4", ".3gp"],
        icons: {
            default: video_icon,
        },
    },
    image: {
        formatName: "image",
        exts: [".png", ".jpg", ".jpeg"],
        icons: {
            default: image_icon,
        },
    },
    compressed: {
        formatName: "compressed",
        exts: [".zip", ".rar"],
        icons: {
            default: compressed_icon,
        },
    },
    document: {
        formatName: "document",
        exts: [".pdf", ".ppt", ".doc", "txt"],
        icons: {
            ".pdf": document_icon_pdf,
            ".ppt": document_icon_ppt,
            ".txt": document_icon_txt,
            ".doc": document_icon_doc,
            "xls": document_icon_xls,

            default: document_icon,
        },
    },

    folder: {
        empty: empty_folder_icon,
        contains: fill_folder_icon,
    },

    unknown: file_unknown,

};

const formats = [
            file_folder_icons.audio,
            file_folder_icons.video,
            file_folder_icons.image,
            file_folder_icons.document,
            file_folder_icons.compressed
];



const getIcon = (ext, empty_folder=false) => {
        /**
         * ext: When you want icon for a folder then you can `ext` leave `undefined`.
         * empty_folder: If folder contains file or then you need to set `true` 
         */
        if (ext === "")
            return file_folder_icons.unknown;

        if (ext != undefined) {
            
            console.log(ext)
            for (let i=0; i < formats.length; i++) {
                let format = formats[i];
                
                if (format.exts.indexOf(ext) !== -1) {
                    let i = format.icons[ext];
                    console.log(format)
                    if (i !== undefined)
                        return i;
                    return format.icons.default;
                }
            }
            return file_folder_icons.unknown;
            
        } else {
            if (empty_folder)
                return file_folder_icons.folder.empty;
            else
                return file_folder_icons.folder.contains;


        }
}


const getFileIcon = (filename) => {
    let ext = filename.substring(filename.lastIndexOf("."));

    if (ext !== filename) {
        return getIcon(ext);
    } else {
        return getIcon("");
    }
}

const getFolderIcon = (empty=false) => {
    return getIcon(undefined, empty);
}
export {getFileIcon, getFolderIcon};