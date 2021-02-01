import '@syncfusion/ej2-base/styles/material.css';
import '@syncfusion/ej2-icons/styles/material.css';
import '@syncfusion/ej2-inputs/styles/material.css';
import '@syncfusion/ej2-popups/styles/material.css';
import '@syncfusion/ej2-buttons/styles/material.css';
import '@syncfusion/ej2-splitbuttons/styles/material.css';
import '@syncfusion/ej2-navigations/styles/material.css';
import '@syncfusion/ej2-layouts/styles/material.css';
import '@syncfusion/ej2-grids/styles/material.css';
import '@syncfusion/ej2-filemanager/styles/material.css';

<title>{{ SITE_NAME }}</title>

import { FileManager } from '@syncfusion/ej2-filemanager';
let fm = new FileManager({
    ajaxSettings: {
        url: 'api/FileManager/FileOperations',
        downloadUrl: 'api/FileManager/Download',
        uploadUrl: 'api/FileManager/Upload',
        getImageUrl: 'api/FileManager/GetImage',
    }
});
fm.appendTo('#filemanager');
